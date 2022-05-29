from django.shortcuts import render, redirect, HttpResponse
from .forms import profform
from .models import person, face
import face_recognition
import cv2
import numpy as np
import os
# Create your views here.

pface = 'no_face'
current_path = os.path.dirname(__file__)


def main(request):
    return render(request, 'main.html')


def scanfunc(request):

    global pface

    known_face_encodings = []
    known_face_names = []

    attend = person.objects.all()
    for att in attend:
        pers = att.image
        image_of_pers = face_recognition.load_image_file(f'media/{pers}')
        pers_face_encoding = face_recognition.face_encodings(image_of_pers)[0]
        known_face_encodings.append(pers_face_encoding)
        known_face_names.append(f'{pers}'[:-4])


    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_names = []
    process_this_frame = True

    while True:

        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    att = person.objects.get(image__icontains=name)
                    if att.attendance:
                        pass
                    else:
                        att.attendance = True
                        att.save()

                    if pface != name:
                        pface = face(pface=name)
                        pface.save()
                        pface = name
                    else:
                        pass

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return HttpResponse('scanner closed', pface)


def ajax(request):
    pface = face.objects.last()
    context = {
        'pface': pface
    }
    return render(request, 'ajax.html', context)


def scan(request):
    try:
        pface = face.objects.last()
        prof = person.objects.get(image__icontains=pface)
    except:
        pface = None
        prof = None
    context = {
        'prof': prof,
        'pface': pface
    }
    return render(request, 'scan.html', context)


def profiles(request):
    prof = person.objects.all()
    context = {
        'profiles': prof
    }
    return render(request, 'people.html', context)


def status(request):
    scanned = face.objects.all()
    pres = person.objects.filter(attendance=True)
    absent = person.objects.filter(attendance=False)
    context = {
        'scanned': scanned,
        'pres': pres,
        'absent': absent
    }
    return render(request, 'status.html', context)


def add_profile(request):
    form = profform
    if request.method == 'POST':
        form = profform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    context = {'form': form}
    return render(request, 'addProfile.html', context)


def delete_prof(request, id):
    profile = person.objects.get(id=id)
    profile.delete()
    return redirect('profiles')


def clear_hist(request):
    hist = face.objects.all()
    hist.delete()
    return redirect('status')


def edit_prof(request, id):
    profile = person.objects.get(id=id)
    form = profform(instance=profile)
    if request.method == 'POST':
        form = profform(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    context = {'form': form}
    return render(request, 'addProfile.html', context)


def edit_prof2(request):
    xd = person.objects.all()
    context = {
        'profiles': xd
    }
    return render(request, 'people.html', context)


def reset(request):
    profile = person.objects.all()
    for prof in profile:
        if prof.attendance:
            prof.attendance = False
            prof.save()
    return redirect('status')


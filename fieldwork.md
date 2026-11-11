# My fieldwork notes

## Conversations

On November 11, 2026, I spoke informally with three classmates during a lunch break about relatives who sometimes forget their medicines. I did not record the exact time, place, or length of the conversations.

- One classmate said a relative sometimes forgets a before-meal medicine while busy with household work.
- Another said a relative sometimes forgets a breakfast-time medicine while commuting and managing work pressure.
- The third said a parent forgets medicine amid daytime responsibilities.

These are classmates' second-hand accounts, not observations I made of the relatives themselves. I have left out names and diagnoses to protect their privacy. I chose my mother as the person I hope to ask to try the reminder prototype, but I have not recorded a test session or feedback from her.

## Prescription-image OCR test

The prescription images in the private `D:\data` folder belong to people I know, and I have their consent to use the images for this project. I processed the first 20 images (`1.jpg` through `20.jpg`) locally with the existing OCR pipeline. It returned 337 text-line detections altogether. I did not display or save the recognized text, and I did not add the images to this repository.

This was a smoke test to check that the pipeline could process the images. I did not compare the output with verified transcriptions, so 337 detections is not an OCR accuracy result. Prescription images are document samples; they do not tell me whether someone took or missed a medicine.

## What I still need to do

- I have not collected a dated set of 20 or more medication-reminder check-ins in `prototype\data.csv`.
- I have tried my own medication during development, but I did not provide dated, anonymized rows or a collection method, so I am not presenting that as a dataset.
- I do not have the two timestamped photos required by the assignment. I will not create or backdate photos, times, or observations.
- I did not record the exact venue, time, or duration of the conversations, and I do not have a recorded surprising observation. I have not filled in those gaps by guessing.
- I still need to run and document a genuine session with my intended tester and make the required screen recording.
- I need to write my own personal reflection.

## Privacy and safety

I will ask for informed agreement before collecting any more information. I will keep the check-in CSV private and avoid recording names, diagnoses, medicine names, doses, phone numbers, or prescription images in it. The prototype is descriptive only; it must not be used to change medication instructions. For questions about a missed dose, I will direct the person to a pharmacist or prescriber.

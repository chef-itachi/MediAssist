# MediAssist reminder check-in

## Why I started this project

I have heard from classmates that some of their relatives forget medicines when they are busy with household work, commuting, or other daily responsibilities. Those conversations made me interested in whether a simple tool could help someone notice patterns in their reminder routine. The reports were second-hand, so I treat them as an early starting point rather than proof of what those relatives experience.

I built a small, local Python prototype that summarizes medication-reminder check-ins by everyday context. It is a starting point for exploring routines, not a medical tool, and it does not recommend changing a dose or schedule. My initial research and fieldwork notes are in [research.md](./research.md) and [fieldwork.md](./fieldwork.md).

## What I built and tried

- I built a local Python tool that reads a CSV and summarizes check-in outcomes and contexts.
- I reviewed existing reminder options and recorded questions that still need to be tested.
- With the image owners' consent, I ran the existing OCR pipeline locally on 20 prescription images from `D:\data`. It returned 337 text-line detections in total. This was a processing check, not an accuracy score: I did not compare the text against verified transcriptions, and neither the images nor recognized text are included here.

The prescriptions are real document samples, but they do not show whether anyone took or missed a dose. Whether they count toward the assignment's 20 observations depends on whether the assignment accepts prescription samples rather than medication-taking observations.

To try the check-in tool, use Python 3.10 or later from the repository root:

```powershell
Copy-Item prototype\data.example.csv prototype\data.csv
# Add only real, consented check-ins to prototype\data.csv.
python prototype\reminder_report.py
```

The CSV columns are `date,time,context,result,delay_minutes`. Each row should represent one real reminder check-in. Valid results are `taken`, `late`, and `missed`; for a late check-in, record the delay in minutes. The tool prints the number of check-ins, outcome counts, and the context with the most missed reminders. It works offline and needs no third-party packages.

## Assignment progress

I have a working prototype, initial research notes, reported conversations with classmates, and a local OCR smoke test on 20 consented prescription samples. I have not yet recorded a test session or feedback from my intended tester. I also do not have the required timestamped fieldwork photos, screen recording, or personal reflection in this repository. I have not added times or evidence that I did not record, and I have not backdated anything.

I cannot recreate the requirement for a first commit within the first hour after the assignment began. I should describe this honestly as progress on the assignment, not claim that every requirement is complete.

## Privacy and limitations

- I keep `prototype\data.csv` on my own device; it is ignored by Git and should not be committed.
- I do not put names, diagnoses, medicine names, doses, contact details, or prescription images in the check-in CSV.
- I collect check-ins only with the person's knowledge and agreement.
- This tool describes the rows entered; it cannot determine why a dose was missed or advise what to do. For missed-dose questions, ask a pharmacist or prescriber.

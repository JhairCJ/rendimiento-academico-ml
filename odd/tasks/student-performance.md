# Student performance analysis
Branch: `feat/student-performance-analysis`; delivery: `ask-on-risk`; runner: Python. Forecast: over 400 authored lines; reviewable conventional commits, no push.

## Specs
- S1: “Rendimiento escolar: explorar la relación entre hábitos y resultados académicos.” Use the chosen Kaggle dataset, explain source and limitations, perform CRISP-DM, exploration, profiling and justified data preparation according to the laboratory rubric.
- S2: “tu solo haz el proyecto y el documento asi excelentes” Develop reproducible Python analysis and update the provided Google Doc with one natural Spanish report based on verified results. The user handles the submission deliverables. Do not invent group contributions.
- S3: “con commits constantes, conventional commits” Commit coherent verified units; do not push without permission.

## Tasks
- T1 [S1,S3] inline: acquire and inspect dataset, document provenance and overlap — completed; source files checked.
- T2 [S1,S3] inline: reproducible exploration, profiling, preparation and checks — in progress; automatic profiles remain pending.
- T3 [S2,S3] inline: report based on results and replace old content in the specified Google Doc — in progress; profiling section and final layout verification remain.

## Log
L1: “dale, ponte a hacer con commits constantes, conventional commits, si quieres anotalo en el agents, toma en cuenta que tienes que trabajar en este link y yo me encargare de hacer los entregables, tu solo haz el proyecto y el documento asi excelentes https://docs.google.com/document/d/1u6Vl9sSZKamb7uFqXpfdsR-OtG0Yz9HRyQ33XZLuIoA/edit?usp=sharing”
L2: The selected Kaggle archive contains Mathematics and Portuguese files. Its data dictionary notes 382 students appear in both; avoid assuming the sum of rows is a count of unique people. The rubric separately awards 20 points to modeling the Banco Berka case.
L3: Initial commit `330e20e` initialized the repository; the feature branch is `feat/student-performance-analysis`.
L4: Kaggle archive inspected: 395 Mathematics rows and 649 Portuguese rows, each with 33 columns, no missing values or exact duplicate rows in the original files. Python environment lacks `ydata_profiling` and plotting libraries.
L5: A reproducible Python analysis prepares one table per subject, adds a readable study-time category, calculates descriptive and bivariate statistics, and creates charts. Public-interface test passed; automatic profiling still requires `ydata_profiling`.
L6: Draft report written to informe.md and the authorized Google Doc; cover preserved and two charts inserted. The report explicitly marks automated profiling as pending.

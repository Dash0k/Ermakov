import pandas as pd
df = pd.read_excel("lab_pi_101.xlsx")

group = input("Введите номер группы: ")

all_marks = df.shape[0]
count_marks_pi101 = len(df[df['Группа'] == group])
count_student_pi101 = df.loc[df['Группа'] == group, 'Личный номер студента'].nunique()

mass_id_stud_pi101 = df.loc[df['Группа'] == group, 'Личный номер студента'].unique()
id_stud_pi101 = ", ".join(map(str, mass_id_stud_pi101))

mass_forms_control = df.loc[df['Группа'] == group, 'Уровень контроля'].unique()
forms_control = ", ".join(mass_forms_control)

all_years1 = df.loc[df['Группа'] == group,'Год'].unique()
all_years = ", ".join(map(str, all_years1))

print("В исходном датасете содержалось", all_marks, "оценок, из них", count_marks_pi101, "оценок относится к группе ПИ101",
"\nВ датасете находятся оценки", count_student_pi101, "студентов ПИ101 с личными номерами:", id_stud_pi101,
"\nИспользуемые формы контроля:", forms_control,
"\nДанные представлены по следующим учебным годам:", all_years)
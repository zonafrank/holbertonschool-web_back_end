export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      const found = newGrades.find((item) => item.studentId === student.id);
      if (found) {
        return { ...student, grade: found.grade };
      }
      return { ...student, grade: 'N/A' };
    });
}

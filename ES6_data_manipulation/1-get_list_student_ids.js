export default function getListStudentIds(studentObjArray) {
  if (!Array.isArray(studentObjArray)) {
    return [];
  }
  return studentObjArray.map((item) => item.id);
}

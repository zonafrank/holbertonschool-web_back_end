export default function getStudentIdsSum (studentObjArray) {
  return studentObjArray.reduce((acc, item) => acc + item.id, 0);
}

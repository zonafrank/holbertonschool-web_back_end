export default function getStudentsByLocation(studentObjArray, city) {
  return studentObjArray.filter((item) => item.location === city);
}

export default function getStudentIdsSum(studentObjArray) {
  return studentObjArray.reduce((acc, item) => {
    return acc + item.id;
  }, 0);
}

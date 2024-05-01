export default function appendToEachArrayValue(array, appendString) {
  let res = []
  for (let item of array) {
    res.push(appendString + item);
  }

  return res;
}

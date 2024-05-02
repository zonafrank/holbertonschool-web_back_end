export default function appendToEachArrayValue(array, appendString) {
  const res = [];
  for (const item of array) {
    res.push(appendString + item);
  }

  return res;
}

export default function cleanSet(set, startString) {
  let result = '';
  if (startString === '') return result;

  for (const item of set) {
    if (item.startsWith(startString)) {
      if (result !== '') {
        result += '-';
      }
      result += item.slice(startString.length);
    }
  }
  return result;
}

export default function (set, array) {
  for (let i = 0; i < array.length; i++) {
    if (!set.has(array[i])) {
      return false;
    }
  }
  return true;
}

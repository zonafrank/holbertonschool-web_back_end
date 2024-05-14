export default function updateUniqueItems(mapObject) {
  if (!(mapObject instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const item of mapObject) {
    const [k, v] = item;
    if (v === 1) {
      mapObject.set(k, 100);
    }
  }
}

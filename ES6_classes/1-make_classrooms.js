import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const classSizes = [19, 20, 34];
  return classSizes.map((val) => new ClassRoom(val));
}

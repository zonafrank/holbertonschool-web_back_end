export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = [...students];
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof (newName) !== 'string') {
      // eslint-disable-next-line no-throw-literal
      throw 'Name must be a string';
    }

    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof (newLength) !== 'number') {
      // eslint-disable-next-line no-throw-literal
      throw 'Length must be a number';
    }

    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStrudentsArr) {
    if (!Array.isArray(newStrudentsArr)) {
      // eslint-disable-next-line no-throw-literal
      throw 'Students must be and array';
    }

    this._students = [...newStrudentsArr];
  }
}

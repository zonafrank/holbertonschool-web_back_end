export default class Currency {
  constructor(code, name) {
    this.name = name;
    this.code = code;
  }

  get code() {
    return this._code;
  }

  set code(val) {
    if (!(typeof (val) === 'string')) {
      // eslint-disable-next-line no-throw-literal
      throw 'code must be a string';
    }
    this._code = val;
  }

  get name() {
    return this._name;
  }

  set name(val) {
    if (!(typeof (val) === 'string')) {
      // eslint-disable-next-line no-throw-literal
      throw 'name must be a string';
    }

    this._name = val;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

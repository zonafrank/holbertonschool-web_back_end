export default class Building {
  constructor(sqft) {
    this.sqft = sqft;

    if (this.constructor !== Building
      && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(val) {
    if (!(typeof (val) === 'number')) {
      // eslint-disable-next-line no-throw-literal
      throw 'sqft must be a number';
    }
    this._sqft = val;
  }

  evacuationWarningMessage() {
    if (this.constructor !== Building
      && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }
}

// msMatchesSelector
((): void => {
  if (!Element.prototype.matches) {
    Element.prototype.matches = Element.prototype.msMatchesSelector
                  || Element.prototype.webkitMatchesSelector;
  }

  if (!Element.prototype.closest) {
    Element.prototype.closest = function closest(s) {
      let el = this;

      do {
        if (el.matches(s)) return el;
        el = el.parentElement || el.parentNode;
      } while (el !== null && el.nodeType === 1);
      return null;
    };
  }
})();

(() => {
  // const common = (() => {
  //   const defParams = {
  //     input: {
  //       self: '.transition-input',
  //     },
  //     cssClass: {
  //       input: {
  //         active: 'transition-input--active',
  //       },
  //     },
  //   };

  //   const transition = {
  //   };
  // })();
})();

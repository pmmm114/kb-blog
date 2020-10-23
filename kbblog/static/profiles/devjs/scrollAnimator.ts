// scroll Lib
function scrollAnimation(selector:string) {
  const _ = this;

  _.$elementNodeList = document.querySelectorAll(selector);
}

scrollAnimation.prototype.init = function init(transitionTiming:string, transitionFunc:string, transitionDelay:string, transformPosition:string) {
  const IOoptions = {
    threshold: 0.4,
  };

  const IOcallback = (entries:Element) => {
    entries.forEach((item) => {
      const entryItem = item;

      if (entryItem.isIntersecting) {
        entryItem.target.style.opacity = 1;
        entryItem.target.style.transform = 'translate(0, 0)';
        entryItem.target.style.webkitTransform = 'translate(0, 0)';
        entryItem.target.style.mozTransform = 'translate(0, 0)';
        entryItem.target.style.msTransform = 'translate(0, 0)';
        entryItem.target.style.oTransform = 'translate(0, 0)';
      }
    });
  };

  const observer = new IntersectionObserver(IOcallback, IOoptions);

  this.$elementNodeList.forEach((item:Element) => {
    let animationType = null;
    let animationDirection = null;
    const elementItem = item;

    animationType = elementItem.getAttribute('scroll-animation');
    animationDirection = elementItem.getAttribute('animation-direction');

    // css transition 초기화
    elementItem.style.transition = 'all';
    elementItem.style.transitionDelay = transitionDelay;
    elementItem.style.transitionDuration = transitionTiming;
    elementItem.style.transitionTimingFunction = transitionFunc;

    if (animationType === 'horizontal') {
      elementItem.style.transform = `translate(${animationDirection === 'LTR' ? -transformPosition : transformPosition}px, 0)`;
      elementItem.style.webkitTransform = `translate(${animationDirection === 'LTR' ? -transformPosition : transformPosition}px, 0)`;
      elementItem.style.mozTransform = `translate(${animationDirection === 'LTR' ? -transformPosition : transformPosition}px, 0)`;
      elementItem.style.msTransform = `translate(${animationDirection === 'LTR' ? -transformPosition : transformPosition}px, 0)`;
      elementItem.style.oTransform = `translate(${animationDirection === 'LTR' ? -transformPosition : transformPosition}px, 0)`;
    } else {
      elementItem.style.transform = `translate(0, ${animationDirection === 'TTB' ? -transformPosition : transformPosition}px)`;
      elementItem.style.webkitTransform = `translate(0, ${animationDirection === 'TTB' ? -transformPosition : transformPosition}px)`;
      elementItem.style.mozTransform = `translate(0, ${animationDirection === 'TTB' ? -transformPosition : transformPosition}px)`;
      elementItem.style.msTransform = `translate(0, ${animationDirection === 'TTB' ? -transformPosition : transformPosition}px)`;
      elementItem.style.oTransform = `translate(0, ${animationDirection === 'TTB' ? -transformPosition : transformPosition}px)`;
    }

    observer.observe(elementItem);
  });
};

export default scrollAnimation;

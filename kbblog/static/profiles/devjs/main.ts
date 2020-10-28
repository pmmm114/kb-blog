import { gsap, ScrollTrigger } from 'gsap/all';
import ScrollAnimation from './scrollAnimator.ts';

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
  const blog = (() => {
    // const getElementById = (id: string): HTMLElement => document.getElementById(id);
    const getQuerySelector = (selector: string): Element => document.querySelector(selector);
    const getQuerySelectorAll = (selector: string): NodeListOf<Element> => document.querySelectorAll(selector);
    const getSelectorString = function getSelectorStringFunc(selector: string): string {
      return selector.substring(1, selector.length);
    };
    const setAddEventListener = function setAddEventListenerFunc(getElementFunc: Function, selector: string, eventType: string, objType: any, listener: Function) {
      let $elements: NodeListOf<Element> = null;

      $elements = getElementFunc(selector);
      if ($elements.length > 0) {
        const eventNamesArray: Array<string> = eventType.split(',');
        for (let eventNamesIndex = 0; eventNamesIndex < eventNamesArray.length; eventNamesIndex += 1) {
          for (let index = 0; index < $elements.length; index += 1) {
            $elements[index].addEventListener(eventNamesArray[eventNamesIndex], (e: typeof objType) => { listener(e); });
          }
        }
      }
    };

    const defClass = {
      common: {
        popup: '.common-popup',
        dimmed: '.dimmed',
        dimmedOn: '.dimmed-on',
        closeBtn: '.close-btn',
      },
      gnb: {
        nav: {
          search: {
            trigger: {
              self: '.gnb__nav-search-trigger',
            },
          },
        },
      },
      input: {
        self: '.transition-input',
      },
      cssClass: {
        input: {
          active: 'transition-input--active',
        },
        popup: {
          active: 'common-popup--active',
        },
      },
    };

    const indexManager = {
      init(): void {
        const _ = this;

        _.bindEvents();
      },
      reInit(): void {
      },
      bindEvents(): void {
      },
    };

    const commonPopup = {
      init(): void {
        const _ = this;

        _.bindEvents();
        _.setDimmed(false);
      },
      reInit(): void {
      },
      bindEvents(): void {
        const _ = this;

        setAddEventListener(getQuerySelectorAll, defClass.common.closeBtn, 'click', MouseEvent, _.closeCommonPopup);
        // getElementByClass(getSelectorString(defClass.common.closeBtn)).addEventListener('click', (e: MouseEvent) => { _.closeCommonPopup(e); });
        // getQuerySelector('[data-popup-target]').addEventListener('click', (e: MouseEvent) => { _.openCommonPopup(e); });
      },
      openCommonPopup(e: MouseEvent): void {
        const _ = this;
        let $popup: Element = null;
        let popupTargetValue: string = null;

        popupTargetValue = (<Element>e.target).closest('[data-popup-target]').getAttribute('data-popup-target');
        $popup = getQuerySelector(`[data-popup-value=${popupTargetValue}]`);
        $popup.classList.add(defClass.cssClass.popup.active);

        _.setDimmed(true);
      },
      closeCommonPopup(e: MouseEvent): void {
        const _ = this;
        let $popup: Element = null;

        $popup = (<Element>e.target).closest(defClass.common.popup);
        $popup.classList.remove(defClass.cssClass.popup.active);

        _.setDimmed(false);
      },
      setDimmed(state: Boolean): void {
        if (state) {
          getQuerySelector(defClass.common.dimmed).style.display = 'block';
          // eslint-disable-next-line no-unused-expressions
          window.getComputedStyle(getQuerySelector(defClass.common.dimmed), null).opacity;
          getQuerySelector(defClass.common.dimmed).classList.add(getSelectorString(defClass.common.dimmedOn));
        } else {
          getQuerySelector(defClass.common.dimmed).classList.remove(getSelectorString(defClass.common.dimmedOn));
          getQuerySelector(defClass.common.dimmed).style.display = 'none';
        }
      },
    };

    const commonTransition = {
      init(): void {
        const _ = this;

        _.bindEvents();
      },
      bindEvents(): void {
        const _ = this;

        setAddEventListener(getQuerySelectorAll, defClass.input.self, 'focus,blur,change', Event, _.transitionEvent);
      },
      transitionEvent(e: Event): void {
        if (e.type === 'focus') {
          e.target.classList.add('transition-input--active');
        } else if (e.target.value) {
          e.target.classList.add('transition-input--active');
        } else {
          e.target.classList.remove('transition-input--active');
        }
      },
    };

    const interactionManager = {
      mainTopGsapOption: {
        scale: 1.2,
      },
      init(): void {
        const _ = this;

        _.getGSAPAnimation('.main-top__background-image');
      },
      getGSAPAnimation(animatingTargetSelector: string) {
        const _ = this;

        let tween = null;
        tween = gsap.to('.main-top__background-image img', _.mainTopGsapOption);

        gsap.registerPlugin(ScrollTrigger);

        ScrollTrigger.create({
          animation: tween,
          trigger: animatingTargetSelector,
          end: '+=400',
          start: 'top top',
          scrub: 0.1,
        });
      },
      reInit(): void {
      },

    };

    const scrollAnimatorManager = {
      timing: '0.4s',
      transitionFunc: 'ease-in-out',
      transitionDelay: '0s',
      scrollTransform: 50,
      attribute: {
        scroll: '[scroll-animation]',
      },
      init(): void {
        const _ = this;

        const scroller = new ScrollAnimation(_.attribute.scroll);
        scroller.init(_.timing, _.transitionFunc, _.transitionDelay, _.scrollTransform);
      },
    };

    const init = (): void => {
      indexManager.init();
      commonPopup.init();
      interactionManager.init();
      scrollAnimatorManager.init();
      commonTransition.init();
    };

    const reInit = (): void => {
      indexManager.reInit();
    };

    return {
      init,
      reInit,
    };
  })();

  ((): void => {
    blog.init();
  })();
})();

// 공통 함수
export const getQuerySelector = (selector: string): Element => document.querySelector(selector);
export const getQuerySelectorAll = (selector: string): NodeListOf<Element> => document.querySelectorAll(selector);
export const getSelectorString = (selector: string): string => selector.substring(1, selector.length);
export const setAddEventListener = (getElementFunc: Function, selector: string, eventType: string, objType: any, listener: Function) => {
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

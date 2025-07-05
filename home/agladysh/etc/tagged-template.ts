// Not tested. Not sure if it will be ever needed. Discard if not.

export type TaggedTemplateArgs = Array<unknown> & { raw: readonly string[] | ArrayLike<string> };

export function isTaggedTemplateArgs(arg0: TaggedTemplateArgs | unknown): arg0 is TaggedTemplateArgs {
  // TODO: Handle arg0.raw being ArrayLike.
  return Array.isArray(arg0) && 'raw' in arg0 && Array.isArray(arg0.raw);
}

export interface TaggedTemplateWrapper {
  (str: TaggedTemplateArgs | string, ...subs: unknown[]): unknown;
}

export const wrap = (
  fn: (str: string, ...args: unknown[]) => unknown,
  ...binds: unknown[]
): TaggedTemplateWrapper => {
  return (str: TaggedTemplateArgs | string, ...subs: unknown[]): unknown => {
    if (isTaggedTemplateArgs(str)) {
      return (...args: unknown[]): unknown =>
        fn.call(this, String.raw(str, ...subs), ...binds, ...args);
    }
    return fn.call(this, str, ...binds, ...subs);
  };
}

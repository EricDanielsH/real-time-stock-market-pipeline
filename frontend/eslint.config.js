import antfu from "@antfu/eslint-config";

export default antfu(
  {
    type: "app",
    typescript: true,
    formmater: true,
    stylistic: {
      indent: 2,
      semi: true,
      quotes: "double",
    },
  },
  {
    rules: {
      "no-console": ["warn"],
      "node/no-process-env": ["error"],
      "perfectionist/sort-imports": [
        "error",
        {
          type: "natural", // Valid sorting type
          internalPattern: ["@/.+"], // Custom internal pattern
          newlinesBetween: "never", // Add newlines between groups
        },
      ],
      "unicorn/filename-case": [
        "error",
        {
          case: "kebabCase",
          ignore: ["README.md"],
        },
      ],
    },
  },
);

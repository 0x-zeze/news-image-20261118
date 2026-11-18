// news-image-20261118 entry: deliver the finished front-page image.
// The image itself is drawn by build_image.py (Pillow) and stored beside
// this file as entry.png; this program only places it at the output path
// the grader reads (/output/entry.png, or MAKEFUN_OUTPUT_DIR locally).
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));

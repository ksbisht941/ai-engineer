/**
 * rename.js — Sequential Image Renamer
 *
 * Recursively walks the dataset directory (train/val/test subfolders),
 * finds all image files, and renames them sequentially:
 *   001.jpg, 002.jpg, 003.jpg, ...
 *
 * A two-pass approach (temp names first) avoids collision when the
 * source and target filenames overlap during renaming.
 *
 * Usage:
 *   node rename.js
 *
 * Config:
 *   ROOT_DIR — path to the root of your organised dataset.
 */

'use strict';

const fs   = require('fs');
const path = require('path');

// ── CONFIG ─────────────────────────────────────────────────────────────────────
const ROOT_DIR         = '../data/output';   // <- adjust to your dataset root
const VALID_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp'];

// ── Helpers ────────────────────────────────────────────────────────────────────

/**
 * Recursively collect leaf directories that contain at least one image.
 * @param {string} dir
 * @returns {string[]}
 */
function getAllTargetFolders(dir) {
  let folders = [];
  const list  = fs.readdirSync(dir);

  list.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat     = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      const subFiles  = fs.readdirSync(fullPath);
      const hasImages = subFiles.some(f =>
        VALID_EXTENSIONS.includes(path.extname(f).toLowerCase())
      );

      if (hasImages) {
        folders.push(fullPath);
      }

      folders = folders.concat(getAllTargetFolders(fullPath));
    }
  });

  return folders;
}

/**
 * Zero-pad a number to *size* digits.  1 → "001"
 * @param {number} num
 * @param {number} [size=3]
 * @returns {string}
 */
function pad(num, size = 3) {
  return String(num).padStart(size, '0');
}

/**
 * Rename all images in *folderPath* to sequential names (001, 002, …).
 * Uses a temp-name pass to avoid clobbering existing files.
 * @param {string} folderPath
 */
function renameFolder(folderPath) {
  const files = fs.readdirSync(folderPath)
    .filter(f => VALID_EXTENSIONS.includes(path.extname(f).toLowerCase()));

  console.log(`\n📁 Processing: ${folderPath} (${files.length} files)`);

  // Pass 1 — rename to unique temp names to avoid conflicts.
  const tempFiles = files.map((file, index) => {
    const oldPath  = path.join(folderPath, file);
    const tempName = `_tmp_${index}_${Date.now()}${path.extname(file)}`;
    const tempPath = path.join(folderPath, tempName);
    fs.renameSync(oldPath, tempPath);
    return tempPath;
  });

  // Pass 2 — rename to final sequential names.
  tempFiles.forEach((tempPath, index) => {
    const ext     = path.extname(tempPath);
    const newName = `${pad(index + 1)}${ext}`;
    const newPath = path.join(folderPath, newName);
    fs.renameSync(tempPath, newPath);
    console.log(`  🔁 → ${newName}`);
  });
}

// ── Main ───────────────────────────────────────────────────────────────────────
function run() {
  if (!fs.existsSync(ROOT_DIR)) {
    console.error(`❌  ROOT_DIR not found: ${ROOT_DIR}`);
    process.exit(1);
  }

  const folders = getAllTargetFolders(ROOT_DIR);
  console.log(`✅  Found ${folders.length} folder(s) with images`);

  folders.forEach(renameFolder);

  console.log('\n🎯  Renaming completed safely!');
}

run();

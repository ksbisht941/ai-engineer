/**
 * structure.js — Dataset Organiser
 *
 * Recursively scans a source directory for images, groups them by document
 * type (inferred from the filename prefix before the first underscore), then
 * splits each group into train / val / test subsets and copies the files into
 * an organised output directory.
 *
 * Expected input filename convention:  <type>_<anything>.<ext>
 *   e.g.  id_front_001.jpg  →  group "id"
 *
 * Output structure:
 *   <OUTPUT_DIR>/
 *     <type>/
 *       train/   (70 % of files)
 *       val/     (15 % of files)
 *       test/    (15 % of files)
 *
 * Usage:
 *   node structure.js
 */

'use strict';

const fs   = require('fs');
const path = require('path');

// ── CONFIG ─────────────────────────────────────────────────────────────────────
const SOURCE_DIR = '../data/input';   // directory that holds raw images
const OUTPUT_DIR = '../data/output';  // where the split dataset is written

const SPLIT_RATIO = {
  train : 0.70,
  val   : 0.15,
  test  : 0.15,
};

const VALID_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp'];

// ── Helpers ────────────────────────────────────────────────────────────────────

/** Create directory (and parents) if it does not already exist. */
function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

/**
 * Derive document type from filename.
 * "id_front_001.jpg" → "id"
 * @param {string} filename
 * @returns {string}
 */
function getDocumentType(filename) {
  return filename
    .split('_')[0]
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '_');
}

/**
 * Recursively collect all image file paths under *dir*, skipping the
 * output directory to prevent re-processing already-organised files.
 * @param {string} dir
 * @returns {string[]}
 */
function getAllImages(dir) {
  let results = [];
  const list  = fs.readdirSync(dir);

  list.forEach(file => {
    const filePath = path.join(dir, file);
    const stat     = fs.statSync(filePath);

    if (stat.isDirectory()) {
      // Skip the output dir to avoid recursive loops.
      if (path.resolve(filePath) === path.resolve(OUTPUT_DIR)) return;
      results = results.concat(getAllImages(filePath));
    } else if (VALID_EXTENSIONS.includes(path.extname(file).toLowerCase())) {
      results.push(filePath);
    }
  });

  return results;
}

/** Fisher-Yates shuffle (returns a new array). */
function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j   = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ── Main ───────────────────────────────────────────────────────────────────────
function organiseDataset() {
  if (!fs.existsSync(SOURCE_DIR)) {
    console.error(`❌  SOURCE_DIR not found: ${SOURCE_DIR}`);
    process.exit(1);
  }

  const imagePaths = getAllImages(SOURCE_DIR);
  console.log(`✅  Found ${imagePaths.length} image(s)`);

  // Group images by document type.
  const grouped = {};
  imagePaths.forEach(filePath => {
    const filename = path.basename(filePath);

    if (!filename.includes('_')) {
      console.warn(`⚠️  Skipping (no underscore in filename): ${filename}`);
      return;
    }

    const docType = getDocumentType(filename);
    if (!grouped[docType]) grouped[docType] = [];
    grouped[docType].push(filePath);
  });

  // Split each group and copy files.
  Object.keys(grouped).forEach(docType => {
    const files      = shuffle(grouped[docType]);
    const total      = files.length;
    const trainCount = Math.floor(total * SPLIT_RATIO.train);
    const valCount   = Math.floor(total * SPLIT_RATIO.val);

    const splits = {
      train : files.slice(0, trainCount),
      val   : files.slice(trainCount, trainCount + valCount),
      test  : files.slice(trainCount + valCount),
    };

    Object.keys(splits).forEach(split => {
      const targetDir = path.join(OUTPUT_DIR, docType, split);
      ensureDir(targetDir);

      splits[split].forEach(srcPath => {
        const filename = path.basename(srcPath);
        fs.copyFileSync(srcPath, path.join(targetDir, filename));
      });
    });

    console.log(`📁  ${docType}: ${total} file(s) → train=${splits.train.length} val=${splits.val.length} test=${splits.test.length}`);
  });

  console.log('\n🎯  Dataset organised successfully!');
}

organiseDataset();

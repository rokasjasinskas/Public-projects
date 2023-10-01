import { writeFile, mkdir, access, constants } from "fs/promises";
import { join } from "path";

const force = process.argv.includes("--force");

const currentDateObj = new Date(); // Create a new Date object
const currentDate = currentDateObj.toISOString().split("T")[0]; // Get the date in the YYYY-MM-DD format
const currentYear = currentDateObj.getFullYear();
const directoryPath = join("reports", `${currentYear}`);
const filePath = join("reports", `${currentYear}`, `${currentDate}.txt`);

const checkAndMakeDirectory = async () => {
  try {
    await access(directoryPath, constants.R_OK | constants.W_OK);
    console.log("Can access directory path");
  } catch {
    console.error("Cannot access directory path");
    await makeDirectory();
    console.log("Directory created");
  }
};

const checkAndCreateFile = async () => {
  let fileExists = true;

  try {
    await access(filePath, constants.R_OK | constants.W_OK);
  } catch (error) {
    fileExists = false;
  }

  if (fileExists) {
    if (force) {
      await overwriteFile();
      console.log("File overwritten");
    } else {
      console.log("File already exists");
    }
  } else {
    await createFile();
    console.log("File created");
  }
};

const makeDirectory = async () => {
  return await mkdir(directoryPath, { recursive: true });
};

const createFile = async () => {
  const data = Buffer.from(process.argv[2]);
  return await writeFile(filePath, data, { flag: "wx" });
};
const overwriteFile = async () => {
  const data = Buffer.from(process.argv[2]);
  return await writeFile(filePath, data, { flag: "w+" });
};

(async () => {
  await checkAndMakeDirectory();
  await checkAndCreateFile();
})();

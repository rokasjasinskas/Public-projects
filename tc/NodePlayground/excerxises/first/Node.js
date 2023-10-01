import { writeFile } from "fs/promises";

const content = "Some content!";
await writeFile("./output.txt", content);


# Exemplar: Edit Files Using Substrings

## Problem Statement
You have a directory containing multiple files of different types, and you want to modify or filter their names based on specific patterns. The goal is to identify files using substrings, edit their names, and list them according to specific rules.

## Files in the Directory
```
janez_profile_11042019.doc  jdoe_profile_07272018.doc  kwood_profile_04022017.doc  pchow_pic_05162019.jpg
jdoe_contact_07292018.csv   kwood_pic_04032017.jpg     list.txt
```

### Requirements:
1. Extract only files that contain the word `profile` in their name.
2. Remove `_profile_` from the name and replace with `_info_`.
3. Change the `.doc` extension to `.txt` for consistency.
4. Output the modified names.

---

### Step 1: Filtering the Files

We can use the `grep` command to list only the files that contain the word `profile`:

```bash
ls | grep "profile"
```

#### Code Output:
```
janez_profile_11042019.doc
jdoe_profile_07272018.doc
kwood_profile_04022017.doc
```

### Explanation
The `grep` command searches for files that include the substring `profile` in their names and filters out the rest.

---

### Step 2: Using `sed` to Replace Substrings

We want to replace `_profile_` with `_info_`:

```bash
ls | grep "profile" | sed 's/_profile_/_info_/'
```

#### Code Output:
```
janez_info_11042019.doc
jdoe_info_07272018.doc
kwood_info_04022017.doc
```

### Explanation
The `sed` command uses the substitution format `s/old_string/new_string/` to find and replace `_profile_` with `_info_` in each filename.

---

### Step 3: Changing File Extensions

Next, we modify the `.doc` extension to `.txt`:

```bash
ls | grep "profile" | sed 's/_profile_/_info_/' | sed 's/\.doc/\.txt/'
```

#### Code Output:
```
janez_info_11042019.txt
jdoe_info_07272018.txt
kwood_info_04022017.txt
```

### Explanation
The second `sed` command replaces `.doc` with `.txt` in the filenames.

---

### Step 4: Combining the Operations

We can combine all these operations into a single command:

```bash
ls | grep "profile" | sed 's/_profile_/_info_/' | sed 's/\.doc/\.txt/' > modified_files.txt
```

#### Code Output:
The modified filenames are saved in a file called `modified_files.txt`:

```
janez_info_11042019.txt
jdoe_info_07272018.txt
kwood_info_04022017.txt
```

### Explanation
This command combines filtering, substring replacement, and file extension changes, and then writes the output to a file.

---

### Step 5: Using a Script to Automate the Process

We can create a Bash script to automate the entire process:

```bash
#!/bin/bash
for file in $(ls | grep "profile"); do
  new_name=$(echo "$file" | sed 's/_profile_/_info_/' | sed 's/\.doc/\.txt/')
  echo "Renaming $file to $new_name"
  mv "$file" "$new_name"
done
```

#### Command to run the script:
```bash
./rename_files.sh
```

### Explanation
The script iterates through each file that matches the `profile` pattern, modifies the name using `sed`, and renames the file using `mv`.

---

### Conclusion
This example shows how to filter and modify filenames using `grep` and `sed`, and automate the process with a Bash script. Understanding how to manipulate filenames and extensions is essential for effective file management.

---

**Note**: Make sure the script has executable permissions before running it:
```bash
chmod +x rename_files.sh
```

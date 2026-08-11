# The Mac Environment Represented by JPMI

The legacy filename for this report is `02_os_version.md`, but the JPMI metadata does **not** contain enough byte-accessible operating-system files in this project to prove one exact macOS build. The more useful standalone question is what kind of Mac environment JPMI itself represents.

## 1. Observation — filesystem and user structure

JPMI reports:

- a GPT-partitioned custody disk;
- an EFI System Partition;
- a journaled HFS+ volume named `Untitled`;
- HFS+ volume identifier `dfe8079582e21400`;
- a normal `Users/roberthunter` home directory;
- application state under `Library`;
- Mail, Contacts, Photos, Cloud/iCloud, mobile-device, database, cache, and preference material;
- filesystem-level Spotlight and DocumentRevisions state.

The public project does not have a byte-readable `/System` tree or a directly readable `SystemVersion.plist` from the restricted JPMI image.

## 2. User-home distribution

| Directory | File rows | Approx. represented size |
|---|---:|---:|
| `Library` | 251,863 | 54.8 GB |
| `Documents` | 119,794 | 23.2 GB |
| `Pictures` | 92,393 | 61.0 GB |
| `Movies` | 61,202 | 9.4 GB |
| `Downloads` | 23,415 | 19.8 GB |
| `Music` | 19,313 | 32.2 GB |
| `Desktop` | 4,654 | 15.1 GB |

The Desktop is therefore only a small fraction of the overall file population.

## 3. Communications and application-state populations

The source characterization reports approximately:

- `128,842` Apple Mail `.emlx` message files;
- `77,907` `.vcf` contact files;
- `12,337` `.icloud`-extension objects;
- `14,365` `.plist` property-list files;
- large JPEG/PNG and media populations;
- approximately `150,022` entries without a conventional filename extension.

The no-extension population includes many databases, caches, application objects, and filesystem structures. It should not be treated as 150,022 unidentified user documents.

## 4. Interpretation

The copy represents a broad Mac account/application environment rather than a flat content export.

This is important to provenance because application and filesystem context can preserve relationships that disappear when documents are extracted into folders for publication.

For example, a message can exist inside an Apple Mail mailbox structure with surrounding database state and attachments; a photograph can exist in Photos with derivatives and metadata; a mobile backup can preserve files from a device that predates the destination Mac volume.

## 5. Historical data can predate the destination

The HFS+ destination reports a creation date of September 26, 2019, yet the account contains years of older files and application data.

There is no contradiction in that fact. A restore, migration, filesystem-aware copy, or other recovery process can place older content onto a newly created destination while retaining many original file timestamps and directory relationships.

The same principle applies to historical Mac diagnostics inside the account: an older MacBook Air diagnostic package can be migrated data and should not automatically identify the 2019 repair-shop machine.

## 6. What can be said about the macOS version?

JPMI's HFS+ structure and application-state artifacts are consistent with the broad macOS era represented by the user data, but **JPMI metadata alone in this public project does not prove one exact macOS version/build**.

The repository therefore does not use another corpus to fill that gap. The precise OS build is left as an open byte-level verification question for the restricted source image.

## 7. Limitation

This report describes what the JPMI metadata itself supports. It does not infer an exact OS build from unrelated evidence, and it does not equate every historical artifact inside `roberthunter` with the physical identity of the laptop later left for repair.

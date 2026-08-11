# 7. Limits and Open Questions

A provenance repository is more credible when it states what the evidence **cannot** answer.

The JPMI material is substantial, but the present project does not have every custody artifact or unrestricted byte-level access to the source E01.

## 1. The exact original copy method is unresolved

The structure is consistent with a broad filesystem-preserving or block-oriented copy lineage, but the current records do not identify the literal repair-shop copy command.

Open questions include:

- Was the first recovery written to a server?
- Was it stored as a raw image, forensic image, logical tree, backup set, or mounted working copy?
- Was the later HFS+ destination restored from an intermediate image?
- Was any partition resized during the process?
- Which utility performed each stage?

The evidence should not be forced into a one-command story unless logs establish it.

## 2. The Crucial X6 is not the original laptop SSD

The 500 GB-class Micron Crucial X6 described in the acquisition record is a **later custody device**.

Its model, serial number, partition geometry, and HFS+ creation date describe that later storage object. They do not identify the original internal SSD hardware in the Mac left for repair.

## 3. The project does not publish the restricted E01 bytes

The GitHub repository is based on received reports and manifests.

This permits strong statements about reported:

- paths;
- hashes;
- timestamps;
- partition structure;
- volume identity;
- CNIDs;
- application/system-state objects.

It does not permit the repository to claim that every source byte was independently re-read during this GitHub build.

## 4. Hashes are manifest evidence unless recomputed from source bytes

The SHA-256 values in this repository are important evidence, but they are received forensic-manifest values.

The public project should therefore say:

> “The JPMI manifest reports this SHA-256.”

rather than implying:

> “This GitHub checkout independently read the restricted JPMI object and computed this SHA-256.”

unless such a re-read actually occurs.

## 5. Old hardware artifacts can be migrated data

The user tree includes historical diagnostic packages whose filenames identify older Apple hardware, including a `roberts-MacBook-Air` name and serial-bearing WirelessDiagnostics folders.

Those artifacts show that data from an older Mac environment is represented inside JPMI.

They do **not** by themselves prove that the older MacBook Air was the computer left at the repair shop in 2019. Mac users can migrate home directories, restore backups, copy diagnostic folders, and carry application data forward across multiple machines.

The repository should therefore treat old hardware diagnostics as **historical source artifacts**, not as automatic identification of the 2019 repair-shop hardware.

## 6. A timestamp is not a person

A modified or accessed timestamp proves that a filesystem field changed. It does not automatically identify:

- Hunter Biden;
- John Paul Mac Isaac;
- a journalist;
- a forensic examiner;
- Spotlight;
- Finder;
- another software process.

Attribution requires object type, event context, surrounding timestamps, logs, and ideally custody records.

## 7. Post-2019 metadata does not equal post-2019 document fabrication

JPMI contains later filesystem activity. That matters.

But the later population identified so far is dominated by system and application metadata, especially Finder and Spotlight-related state.

A responsible conclusion is:

> The copy was later mounted, browsed, indexed, or examined.

A much stronger claim such as:

> Someone inserted large numbers of substantive files after April 2019.

requires file-level evidence beyond the later metadata clusters presently identified.

## 8. The empty deleted-file catalog is not proof that nothing was deleted

The source reports an empty deleted-file catalog and large unallocated ranges.

On HFS+, deletion history is not necessarily recoverable as a neat catalog of every deleted object. Unallocated space can contain remnants, overwritten fragments, or no useful recoverable data at all.

The project should not equate an empty deleted catalog with “no deletions ever occurred.”

## 9. File counts are not unique-content counts

One underlying item can appear as:

- an original file;
- an email attachment;
- a thumbnail;
- a Photos derivative;
- a cache entry;
- a duplicate download;
- an alias/hard-link representation.

This is why the project tracks paths, CNIDs, sizes, and hashes separately.

## 10. Timezones remain a normalization issue

The received reports use a mixture of labeled local times and UTC-oriented timeline values. Some database fields do not preserve timezone metadata.

Before asserting exact minute-level sequencing across report families, the relevant fields should be normalized against the original source-report convention.

## Highest-value missing evidence

The following materials would materially strengthen the JPMI provenance chain:

1. original repair-shop recovery logs;
2. first-copy hashes;
3. repair-shop server records, if applicable;
4. source/destination device serials from each intermediate step;
5. copy-tool or imaging logs;
6. contemporaneous custody notes;
7. the restricted E01 for independent read-only verification;
8. complete acquisition worksheets associated with `HB-IMAGE-2022-04-29.E01`;
9. normalized timezone documentation for each received report family.

## Publication rule

When a conclusion is not directly established, this repository should use wording such as:

- “the evidence is consistent with…”
- “the metadata supports…”
- “the current records do not establish…”
- “the exact mechanism remains unresolved…”

That is not weakness. It is the difference between forensic reporting and advocacy.

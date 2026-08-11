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

## 2. The 2022 acquisition record and 2024 last-write are not reconciled

The delivered acquisition record identifies:

```text
HB-IMAGE-2022-04-29.E01
reported_at: 2022-04-29
```

The delivered HFS+ volume metadata also reports:

```text
volume_last_write_reported: 2024-11-21 17:40:22 CST
```

An immutable E01 actually acquired in April 2022 cannot later acquire a November 2024 filesystem write.

The current records therefore require at least one missing fact: a later acquisition, a later working copy, source-device activity after 2022, regenerated/mixed reports, or a mislabeled date/provenance field.

This repository does **not** currently establish which explanation is correct.

Until the underlying acquisition worksheets and report lineage are reconciled, the project should preserve both reported values and label the combination an **open chronology discrepancy**.

## 3. The Crucial X6 is not the original laptop SSD

The 500 GB-class Micron Crucial X6 described in the acquisition record is a **later custody device**.

Its model, serial number, partition geometry, and HFS+ creation date describe that later storage object. They do not identify the original internal SSD hardware in the Mac left for repair.

## 4. The project does not publish the restricted E01 bytes

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

## 5. Hashes are manifest evidence unless recomputed from source bytes

The SHA-256 values in this repository are important evidence, but they are received forensic-manifest values.

The public project should therefore say:

> “The JPMI manifest reports this SHA-256.”

rather than implying:

> “This GitHub checkout independently read the restricted JPMI object and computed this SHA-256.”

unless such a re-read actually occurs.

## 6. Old hardware artifacts can be migrated data

The user tree includes historical diagnostic packages whose filenames identify older Apple hardware, including a `roberts-MacBook-Air` name and serial-bearing WirelessDiagnostics folders.

Those artifacts show that data from an older Mac environment is represented inside JPMI.

They do **not** by themselves prove that the older MacBook Air was the computer left at the repair shop in 2019. Mac users can migrate home directories, restore backups, copy diagnostic folders, and carry application data forward across multiple machines.

The repository should therefore treat old hardware diagnostics as **historical source artifacts**, not as automatic identification of the 2019 repair-shop hardware.

## 7. A timestamp is not a person

A modified or accessed timestamp proves that a filesystem field changed. It does not automatically identify:

- Hunter Biden;
- John Paul Mac Isaac;
- a journalist;
- a forensic examiner;
- Spotlight;
- Finder;
- another software process.

Attribution requires object type, event context, surrounding timestamps, logs, and ideally custody records.

## 8. Post-2019 metadata does not equal post-2019 document fabrication

JPMI contains later filesystem/system-state timestamps. That matters.

But the later population identified so far is dominated by system and application metadata, especially Finder and Spotlight-related state.

A responsible conclusion is:

> The represented copy lineage contains evidence of later filesystem or system-state activity.

A much stronger claim such as:

> Someone inserted large numbers of substantive files after April 2019.

requires file-level evidence beyond the later metadata clusters presently identified.

Because of the unresolved 2022/2024 chronology, the repository should also avoid assigning every later timestamp to one specific physical disk or image stage unless that stage is established by the source reports.

## 9. The empty deleted-file catalog is not proof that nothing was deleted

The source reports an empty deleted-file catalog and large unallocated ranges.

On HFS+, deletion history is not necessarily recoverable as a neat catalog of every deleted object. Unallocated space can contain remnants, overwritten fragments, or no useful recoverable data at all.

The project should not equate an empty deleted catalog with “no deletions ever occurred.”

## 10. File counts are not unique-content counts

One underlying item can appear as:

- an original file;
- an email attachment;
- a thumbnail;
- a Photos derivative;
- a cache entry;
- a duplicate download;
- an alias/hard-link representation.

This is why the project tracks paths, CNIDs, sizes, and hashes separately.

## 11. Timezones remain a normalization issue

The received reports use a mixture of labeled local times and UTC-oriented timeline values. Some database fields do not preserve timezone metadata.

Before asserting exact minute-level sequencing across report families, the relevant fields should be normalized against the original source-report convention.

## Highest-value missing evidence

The following materials would materially strengthen the JPMI provenance chain:

1. **the complete acquisition/report lineage needed to reconcile the 2022 E01 record with the 2024 reported last-write;**
2. original repair-shop recovery logs;
3. first-copy hashes;
4. repair-shop server records, if applicable;
5. source/destination device serials from each intermediate step;
6. copy-tool or imaging logs;
7. contemporaneous custody notes;
8. the restricted E01 for independent read-only verification;
9. complete acquisition worksheets associated with `HB-IMAGE-2022-04-29.E01`;
10. normalized timezone documentation for each received report family.

## Publication rule

When a conclusion is not directly established, this repository should use wording such as:

- “the evidence is consistent with…”
- “the metadata supports…”
- “the current records do not establish…”
- “the exact mechanism remains unresolved…”

That is not weakness. It is the difference between forensic reporting and advocacy.

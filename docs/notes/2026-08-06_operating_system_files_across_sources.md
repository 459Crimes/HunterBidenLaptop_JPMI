# Operating-System Files Across Sources

## Scope

This note separates exact byte identity from filesystem structure and operating-system inference across 0728, APFS, GAI, and JPMI. A matching filename or directory is not treated as proof of a matching source object; SHA-256 identity and provenance remain separate.

## APFS Source

The APFS source (`rhb_drive`, source 1) is a GPT image containing an APFS boot volume and a separate HFS+ Mojave installer partition. The readable APFS `System/Library/CoreServices/SystemVersion.plist` identifies:

- macOS `10.14.6`
- build `18G103`

The APFS image also contains normal macOS system/application trees, recovery and CCC-related material, Preboot content, and user data. The HFS+ partition contains installer material and should not be conflated with the installed APFS system.

## GAI Source

The GAI source (`gai_drive`, source 116) is a truncated HFS+ volume image. Its readable `System/Library/CoreServices/SystemVersion.plist` also identifies macOS `10.14.6`, build `18G103`. It contains a conventional macOS system tree, applications, user home data, HFS+ metadata, and recovery/Preboot-related material.

The image is mounted read-only through the documented padded HFS+ device-mapper procedure because its secondary volume header lies beyond the truncated image EOF. The synthetic pad permits filesystem access but does not recover bytes beyond the acquired image.

## 0728 Root Material

The 0728 source contains more than `Extra Found Files`. Its recovered `Root` branch contains approximately `422` cataloged files, including:

- `BaseSystem.dmg`
- `InstallESD.dmg`
- `AppleDiagnostics.dmg`
- installer chunklists and manifests
- `macOS Install Data`
- Preboot installer files
- installer logs and compatibility metadata

This is installer/recovery/staging material rather than a normal installed system volume. The recovered `SystemVersion.plist` and `InstallInfo.plist` variants in the Root branch are not currently valid standalone plist data, so they do not independently establish a build number. The installer contents are consistent with the Mojave-era `10.14.6` / `18G103` environment identified directly in APFS and GAI, but exact version attribution for every carved Root artifact remains inferential.

Of the `381` Root files with SHA-256 values, only a small number have exact hash overlaps with the other source inventories: `10` with APFS, `9` with GAI, and `7` with JPMI. Most installer payloads are unique to the 0728 branch.

## JPMI Source

JPMI is materially different from the other sources. It is a metadata/hash inventory rather than a readable byte source in this project. The JPMI records describe:

- GPT partition structure;
- an EFI partition;
- a large HFS+ volume named `Untitled`;
- a conventional `roberthunter` home directory;
- `System`, `Library`, `Applications`, `Users`, and other normal macOS paths;
- HFS+ journal, catalog, CNID, and extended metadata structures;
- Spotlight, DocumentRevisions, caches, application state, and system artifacts.

This strongly supports JPMI being a substantial HFS+ Mac-volume witness, not merely a copied home directory. However, JPMI does not currently provide recoverable bytes with which to independently inspect `SystemVersion.plist`, installer payloads, kernel metadata, or exact build identifiers.

Therefore:

- JPMI can establish that macOS system/application material and a native HFS+ volume structure were present.
- JPMI cannot currently establish an exact macOS version or build from the available project evidence.
- JPMI's HFS+ format is consistent with a pre-APFS or HFS+ destination/recovery volume, but filesystem format alone does not identify the installed macOS release.
- JPMI path/timestamp evidence may reflect later server staging, restoration, indexing, or examination activity and must not automatically be treated as original OS activity.

## Comparative Conclusion

APFS and GAI independently identify the same Mojave release/build (`10.14.6`, `18G103`). 0728 contains matching-era installer/recovery artifacts but is a distinct recovered branch. JPMI contains extensive native macOS/HFS+ system evidence but lacks accessible bytes for exact OS-version confirmation.

The strongest supported statement is therefore:

> APFS and GAI directly document macOS 10.14.6 build 18G103; 0728 contains compatible Mojave installer/recovery material; JPMI documents a substantial HFS+ macOS volume but does not, from the available metadata-only evidence, prove an exact operating-system version or build.

No source evidence was modified by this analysis.

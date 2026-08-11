# OS Version — JPMI Evidence

**Status: DRAFT for investigator review.**

## 1. What the JPMI metadata shows

- The data partition is **journaled HFS+** named `Untitled`, volume identifier `dfe8079582e21400`.
- GPT layout with an EFI System Partition and an HFS+ data partition.
- The accessible inventory is the `roberthunter` home directory plus filesystem structural records. It contains **no `/System` or `/Applications` bytes** and no readable `SystemVersion.plist`.
- Application-state and diagnostics artifacts are Mojave-era consistent: `com.apple.touristd` Mojave icon assets, DrFone tooling, CoreCapture/AirPortBrcm4360 wireless diagnostics, and the 2016 diagnostic formats.
- The JPMI volume was created/reconstructed **2019-09-26** (reported); HFS+ on the destination does not independently fix the installed macOS release.

## 2. Cross-source context (not from JPMI bytes)

- APFS source: `SystemVersion.plist` = macOS **10.14.6**, build **18G103**.
- GAI source: `SystemVersion.plist` = macOS **10.14.6**, build **18G103**.
- 0728 Root: Mojave installer/recovery material consistent with the same era.

These are the byte-readable confirmations of the same lineage; they are not JPMI-internal evidence.

## 3. Conclusion

JPMI metadata alone **cannot prove** an exact macOS version or build. The structure and application-state evidence are **consistent with macOS 10.14 (Mojave)**, matching the 10.14.6 / 18G103 build independently read from APFS and GAI. Exact attribution for the JPMI volume requires byte-level inspection via the readable cross-source routes or the restricted source image.


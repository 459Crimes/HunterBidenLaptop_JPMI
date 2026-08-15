# The Mac Shop (April 2019 recovery)

> **Hatnote.** This article is about the **Wilmington repair event** that starts the JPMI chain. For later copies, see [Copy lineages](COPY_LINEAGES.md). For the full date table, see [Timeline](06_timeline_and_handling.md).

**The Mac Shop** (legal name in public business records: **The Mac Shop, Inc.**) was a Mac repair shop in Wilmington’s **Trolley Square** neighborhood, operated by **John Paul Mac Isaac**. Delaware court opinions recite that Hunter Biden presented damaged Apple laptops there on **12 April 2019**.

## Address and premises

| Field | Public record |
|---|---|
| Street | **21A Trolley Square** (also written 21 / 21a Trolley Sq) |
| City | Wilmington, Delaware **19806** |
| Neighborhood | Trolley Square shopping center |
| EIN (business-directory class) | 27-2084791, Delaware corporation, address first seen 2009 in some EIN aggregators |
| Established (self-description in old business listings) | 2010, Greater Wilmington Mac service |
| Closed | **November 2020** “for the foreseeable future” after the laptop story ([Delaware Business Now](https://www.delawarebusinessnow.com/news/analysis/john-paul-s-mac-shop-closes-for-the-foreseeable-future/article_3a7cc4a7-fd6e-520a-9f0b-566898306935.html); customer-recommendation note: [dannyschweers.com](https://dannyschweers.com/recommended-apple-macintosh-repair-wilmington-delaware/)) |

Yelp and similar directories still list the closed shop at [21A Trolley Sq](https://www.yelp.com/biz/the-mac-shop-wilmington) and host **customer photos of the storefront/interior** — those are premises pictures, not forensic exhibits.

CBS photographed Mac Isaac **inside the shop on 14 October 2020**, the day the *New York Post* story ran ([CBS](https://www.cbsnews.com/news/hunter-biden-laptop-new-york-post-story/), photo: Bo Erickson). ABC later ran a **21 October 2020 file photo of the storefront** ([ABC News](https://abcnews.com/US/hunter-biden-files-counter-claims-computer-repairman-handling/story?id=97918174)). See [Portraits and premises](PORTRAITS.md).

Mac Isaac told CBS the shop had indoor cameras with **~two months** retention and that he did not grasp the laptops’ significance until after that footage had rotated off.

## The three-laptop event

The Delaware Supreme Court’s 2025 opinion (including the dissent’s summary of the Second Amended Complaint) recounts:

1. **Three damaged laptops** were presented.
2. Mac Isaac supplied a **keyboard** that made **one** machine usable.
3. **One** machine was considered **unrecoverable**.
4. The **remaining** laptop was left for **data recovery**.
5. A **repair authorization** was signed ([Quote #7469](EXHIBITS.md)).

This is why “the laptop” is a journalistic shorthand, not a serial-number identification. JPMI’s `roberthunter` tree can contain **migrated** and **multi-device** material (iPhone/iPad backups, iCloud, older `roberts-MacBook-Air` diagnostics). Older artifacts do **not** prove they were created on the one physical Mac left for recovery.

## 13 April 2019 — customer external drive

The next day, at Mac Isaac’s request, Biden returned with an **external hard drive** for the recovered data. Court opinions state Mac Isaac completed the recovery/transfer that day and contacted Biden.

Mac Isaac later said he first copied recoverable data to his **secure store server**, then from that server onto the customer drive. This project **accepts that as the operative technical account** and labels it as **his declaration**. The repository does not hold server logs, the server image, copy-tool history, or first-generation hashes. No contradictory evidence has surfaced here; independent verification would require those server-side records.

```text
Damaged laptop (retained for recovery)
        |
        v
Mac Isaac store server / recovery workspace     [logs not held]
        |
        +--> customer-supplied external hard drive
        |
        +--> later preservation / FBI / safekeeping copies
```

The server-first workflow is technically important: later Mac Isaac copies **need not preserve the original laptop’s native disk geometry** while still preserving a broad user environment. That is one reason the later Crucial X6 is described as a **custody medium**, not “the laptop SSD.”

## Invoice and non-pickup

Mac Isaac sent an **$85** electronic invoice on **17 April 2019**. Pleadings state the laptop and external drive were not reclaimed or paid for despite contact attempts.

The signed in-shop form is **Quote #7469** (same $85, bill-to Hunter Biden, email `rhbdc@icloud.com`, scope including “recover data to store server and contact customer when complete”). The **emailed** invoice is a later CRM/iCloud object: government **GTX 40** in the 2024 Delaware gun trial (“The Mac Shop Invoice Emailed to rhbdc@icloud.com”). Photographs and the distinction: [Exhibits](EXHIBITS.md). Congressional FBI/laptop reports: [Congress](CONGRESS.md).

JPMI’s substantive user/application modifications are overwhelmingly **before** this repair window. Later activity in the current reports is sparse and metadata-dominated. Nothing in the JPMI reporting analyzed here establishes hacking or injection of substantive external user files during April–July 2019. See [Integrity](INTEGRITY.md).

## What the shop event is not

- It is not a proof of the **make/model/serial of the retained laptop**. Historical WirelessDiagnostics packages naming `roberts-MacBook-Air` / serial `C02S953UH3QF` show **older Mac data is represented**; they do not independently identify the 2019 drop-off machine ([device report](../build/reports/01_computer_information.md)).
- It is not a proof of the **literal copy command**.
- It is not the FBI seizure (that is **9 December 2019**).

## See also

- [Exhibits](EXHIBITS.md)
- [People](PEOPLE.md)
- [Chain of custody](03_chain_of_custody.md)
- [Limits](07_limits_and_open_questions.md)

# AZLibrary

Download Books Use [Anna’s Archive](https://annas-archive.li/) And Rename. Include Pirate Library Mirror and so on.



## Resource Description

- torrent: Torrents (books)
- index: Index for renaming (exported from the database)
- tree: Index for renaming (from actual files)
- other: Other files for communication and learning
  - reference: Reference materials
  - process: Process files used during handling
  - torrent-index: Torrents (database)



## Steps



### 1. Download Books

- Install BT download software, recommended:  [qBittorrent](https://www.qbittorrent.org/download)
- Download via torrents: Use only torrent-zlib1, torrent-zlib2
- Once a torrent is downloaded, you can rename it



### 2. Rename

#### Method 1: Rename using index (source: index directory of this resource)

1. Install the Python environment, install the required Python package: `pip install pathvalidate`.
2. Run the  `rename_by_txt.py` script.
   - First, select the folder where the downloaded books are stored.
   - Then, select the index txt file: Pay attention to the correspondence with the torrent.
   - Finally, select the folder for the renamed output files.
3. After the script runs, check the log and manually handle any files that failed to rename.

> Note:
>
> There are two index files, because they exceeded 100MB, they are split into two parts. Pay attention during renaming.
>



#### Method 2: Rename using tree (source: tree directory of this resource)

1. Install the Python environment.
2. Run the  `rename_by_tree.py`  script.
   - First, select the folder where the downloaded books are stored.
   - Then, select the index txt file: Pay attention to the correspondence with the torrent.
   - Finally, select the folder for the renamed output files.
3. After the script runs, check the log and manually handle any files that failed to rename.

> Note: Continuously updating.

.

#### Comparison

|          | Advantages                      | Disadvantages                                                |
| -------- | ------------------------------- | ------------------------------------------------------------ |
| Method 1 | -                               | The index number is larger than the actual file number, highly redundant |
| Method 2 | Generated based on actual files | -                                                            |



### 3. Others

* Renamed file name format: ZlibID-title.extension

  ```sh
  Example: 1-Руководство по не знаю чему 123213.fb2.zip
  If you do not like this format, you can adjust the script yourself
  ```

* pilimi-zlib-0-119999.torrent as the first torrent, downloads quickly, but mostly  fb2.zip

* zlib1: release

  * 6.15TB

  * file: 2180K



### To Do

- [ ] Local Book Searcher
- [ ] zlib3
- [ ] duxiu



## Milestone

* 2024.12.04: zlib2 release
* 2024.07.04: zlib1 release

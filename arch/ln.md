# The `ln` Command ... 

`ln` is used to create hard links and symbolic links. 

**What are Hard links?**

**Hard links** are a synced carbon-copy of a file that refers directly to the inode of a file. 

**What are symbolic Links?**

**Symbolic Links** are like pointers which directly refers to the inode of a file like a shortcut. 

**What are inodes?**

An **inode** is data structure which stores different attributes of a file like it's disk block location, metadata, owner, and much more. 

The `ln` command creates hard link by default. To create symbolic link you need to add `-s` or `--symbolic` switch to the command. 

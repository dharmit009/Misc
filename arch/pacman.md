# Pacman Guide ...

Never run `pacman` without root privileges. 

## Update your Databases. 

``` 
sudo pacman -Sy

``` 
## Update and Upgrade Databases. 

``` 
sudo pacman -Sy

```

## Custom Respositories. 

To update your config file in `/etc/`

## List All Applications Installed on the system. 

```
sudo pacman -Qs

```

## List All Applications files on the system. 

```
sudo pacman -Ql

```

## Find applications by using commands even if they are not installed. 

```
sudo pacman -Fy <path/to/command/>

```

**Example:**

```
sudo pacman -Fy /usr/bin/netstat

```

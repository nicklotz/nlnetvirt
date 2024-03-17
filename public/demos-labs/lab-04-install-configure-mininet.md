# Lab 04: Install and Configure Vagrant and Mininet

**NOTE:** This lab assumes an Ubuntu Linux host that supports installing VirtualBox as a hypervisor. If you are on another Linux distro or Windows/Mac, take note of the package manager commands (i.e. **apt**) and use the installation tools appropriate for your system.

## A. Install VirtualBox

1. In a terminal, update the package manager.

```
sudo apt update
sudo apt-get update
```

2. Install virtualbox and its supporting tools.

```
sudo apt-get install -y virtualbox
sudo apt-get install -y virtualbox-ext-pack
sudo apt-get install -y virtualbox-guest-utils
```

3. You might be prompted to except Oracle's license for the extension tools. Select agree/ok if prompted.

## B. Install Vagrant

Vagrant is a tool developed by HashiCorp for building and maintaining out-of-the-box VM appliances. Reminder that this section's instructions assume an Ubuntu Linux host. Follow the instructions [here](https://developer.hashicorp.com/vagrant/downloads#linux) for installing on your platform.

1. Download HashiCorp's signing key to verify the vagrant packages.

```
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

2. Add the needed repos to the apt package manager.

```
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
```

3. Update the package manager.

```
sudo apt update
```

4. Install vagrant.

```
sudo apt install -y vagrant
```

## C. Configure a virtual machine to host mininet

1. Create a directory to host your VM configuration.

```
mkdir ~/mininet-vm
```

2. Change to the VM configuration directory.

```
cd ~/mininet-vm
```

3. Initialize a new Ubuntu VM with vagrant.

```
vagrant init ubuntu/jammy64
```

4. Modify the **Vagrantfile** created by the previous command. Add the following configuration text to the file (just choose somewhere among the rest of the commented lines). Make sure the indentation is consistent with the surrounding lines.

```
  # ... some commented-out lines above
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 2
  end
  # ... some commented-out lines below
```

5. Bring up the new VM.

```
vagrant up
```

6. SSH into the new VM.

```
vagrant ssh
```

**Note:** Make sure you're still in the **~/mininet-vm** directory when you run the `vagrant up` and `vagrant ssh` commands.

## D. Install and test mininet on the Vagrant VM

Make sure to SSH into the vagrant VM if you haven't already done so (step C.6).

1. Clone the mininet source repository.

```
git clone https://github.com/mininet/mininet
```

2. Change into the source directory.

```
cd mininet/
```

3. Check out a recent tagged commit (marking a release).

```
git checkout -b mininet-2.3.1b4 2.3.1b4
```

4. Navigate back out of the source directory.

```
cd ..
```

5. Install mininet and its supporting tools (OpenFlow, POX). Installation can take a few minutes. This is a good opportuity to grab a snack.

```
mininet/util/install.sh -a
```

6. After installation completes, test mininet and its networking capabilities.

```
sudo mn --test pingall
```

7. List directory contents to see what's been installed alongside mininet.

```
ls -l
```

# Create GCP instance
gcloud compute instances create "mininet-server" --zone=us-central1-a --machine-type=n1-standard-16 --boot-disk-size=500GB --enable-nested-virtualization --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud
gcloud compute ssh mininet-server --zone=us-central1-a

# Install virtualbox
sudo apt update
sudo apt-get update
sudo apt-get install -y virtualbox
sudo apt-get install -y virtualbox-ext-pack
sudo apt-get install -y virtualbox-guest-utils

# Install vagrant
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant

# Configure mininet vagrant box
mkdir mininet-vm
cd mininet-vm
vagrant init ubuntu/bionic64

# Add/modify Vagrantfile
config.vm.provider "virtualbox" do |vb|
  vb.memory = "1024"
  vb.cpus = 2
end
config.vm.provision "shell", inline: <<-SHELL
  sudo apt-get update
  sudo apt-get install -y mininet
SHELL

# Start and Connect to vagrnat
vagrant up
vagrant ssh

# Test mininet
sudo mn --test pingall


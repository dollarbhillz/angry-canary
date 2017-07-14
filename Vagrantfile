# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'pathname'

project_path = Pathname(__FILE__).dirname
conf_directory = project_path + "conf"
ssh_key_path = Pathname(conf_directory) + "provision_ssh_key"

if not Pathname(ssh_key_path).exist?
    puts("No public key found at #{ssh_key_path}!")
    exit
end

Vagrant.configure("2") do |config|
    config.vm.box = "generic/rhel7"
    config.vm.box_version = "1.0.4"
    config.vm.define "flask_app" do |flask|
        flask.vm.network "private_network",
            ip: "192.168.122.101"
    end

    config.vm.provision "file",
        source: "conf/provision_ssh_key",
        destination: "/home/vagrant/user_key"
    config.vm.provision "shell",
        path: "bin/install_provisioning_account",
        env: { "PROVISION_USER" => "mr_provisioner" }
end

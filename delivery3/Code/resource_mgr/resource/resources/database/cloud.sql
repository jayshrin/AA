SET foreign_key_checks = 0;
DROP DATABASE if exists MIAAS;
CREATE DATABASE MIAAS; 

USE MIAAS;
CREATE TABLE users(
	user_id INTEGER NOT NULL,
	PRIMARY KEY (user_id)
);

CREATE TABLE clouds(
	cloud_id INTEGER NOT NULL,
	ip VARCHAR(15),
	PRIMARY KEY (cloud_id)
);

CREATE TABLE nodes(
	cloud_id INTEGER NOT NULL,
	node_id INTEGER NOT NULL,
	cpu_cap INTEGER NOT NULL,
	ram_cap INTEGER NOT NULL,
	storage_cap INTEGER NOT NULL,
	PRIMARY KEY (cloud_id,node_id),
	FOREIGN KEY (cloud_id) REFERENCES clouds(cloud_id)
);

CREATE TABLE hubs(
	hub_id INTEGER NOT NULL,
	cloud_id INTEGER NULL,
	node_id INTEGER NULL, -- NULL node or cloud id indicete unattached hubs
	device_cap INTEGER NOT NULL,
	PRIMARY KEY (hub_id),
	FOREIGN KEY (cloud_id,node_id) REFERENCES nodes(cloud_id,node_id)
);

CREATE TABLE mobiles(
	mobile_id INTEGER NOT NULL,
	hub_id INTEGER, -- null hub ids indicate unconnected mobile devices
	platform VARCHAR(10) NOT NULL
		CHECK (platform IN ("Android","iOS")),
	version VARCHAR(10) NOT NULL,
	manufacturer VARCHAR(10) NOT NULL,
	model VARCHAR(10) NOT NULL,
	PRIMARY KEY (mobile_id),
	FOREIGN KEY (hub_id) REFERENCES hubs(hub_id)
);

CREATE TABLE vms(
	cloud_id INTEGER NOT NULL,
	node_id INTEGER NOT NULL,
	vm_id INTEGER NOT NULL,
	cpu INTEGER NOT NULL,
	ram INTEGER NOT NULL,
	storage INTEGER NOT NULL,
	PRIMARY KEY (vm_id),
	FOREIGN KEY (cloud_id,node_id) REFERENCES nodes(cloud_id,node_id)
);

CREATE TABLE emulators(
	vm_id INTEGER NOT NULL,
	em_id INTEGER NOT NULL,
	platform VARCHAR(10) NOT NULL
		CHECK (platform IN ("Android","iOS")),
	version VARCHAR(10) NOT NULL,
	manufacturer VARCHAR(10) NOT NULL,
	model VARCHAR(10) NOT NULL,
	PRIMARY KEY (vm_id,em_id),
	FOREIGN KEY (vm_id) REFERENCES vms(vm_id)
);

CREATE TABLE vm_usage(
	user_id INTEGER NOT NULL,
	vm_id INTEGER NOT NULL,
	launch TIMESTAMP NOT NULL,
	terminate TIMESTAMP,
	PRIMARY KEY (user_id,vm_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (vm_id) REFERENCES vms(vm_id)
);

CREATE TABLE em_usage(
	user_id INTEGER NOT NULL,
	vm_id INTEGER NOT NULL,
	em_id INTEGER NOT NULL,
	launch TIMESTAMP NOT NULL,
	terminate TIMESTAMP,
	PRIMARY KEY (user_id,vm_id,em_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (vm_id,em_id) REFERENCES emulators(vm_id,em_id)
);

CREATE TABLE mobile_usage(
	user_id INTEGER NOT NULL,
	mobile_id INTEGER NOT NULL,
	launch TIMESTAMP NOT NULL,
	terminate TIMESTAMP,
	PRIMARY KEY (user_id,mobile_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (mobile_id) REFERENCES mobiles(mobile_id)
);

CREATE TABLE hub_usage(
	user_id INTEGER NOT NULL,
	hub_id INTEGER NOT NULL,
	launch TIMESTAMP NOT NULL,
	terminate TIMESTAMP,
	PRIMARY KEY (user_id,hub_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (hub_id) REFERENCES hubs(hub_id)
);
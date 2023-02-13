provider "local" {
  version = "1.0.0"
}

module "local_network" {
  source = "./local_network"
}

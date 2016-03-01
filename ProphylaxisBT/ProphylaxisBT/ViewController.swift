//
//  ViewController.swift
//  ProphylaxisBT
//
//  Created by Derek De Young on 1/23/16.
//  Copyright © 2016 Prophylaxis. All rights reserved.
//

import UIKit
import CoreBluetooth

class ViewController: UIViewController, CBCentralManagerDelegate, UITableViewDelegate, UITableViewDataSource {
    
    var centralManager: CBCentralManager?
    var peripherals = [CBPeripheral]()
    var timer: NSTimer?

    @IBOutlet weak var tableView: UITableView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.tableView.dataSource = self
        self.tableView.delegate = self
        
        self.centralManager = CBCentralManager(delegate: self, queue: nil)
    }
    
    
    @IBAction func refreshTapped(sender: AnyObject) {
        self.peripherals.removeAll()
        self.tableView.reloadData()
        
        startScan()
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.peripherals.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = UITableViewCell()
        let peripheral = self.peripherals[indexPath.row]
        cell.textLabel!.text = peripheral.name
        return cell
    }

    
    func startScan(){
        self.timer?.invalidate()  //stop previous timer if there is one
        self.centralManager?.scanForPeripheralsWithServices(nil, options: nil)
        self.timer = NSTimer.scheduledTimerWithTimeInterval(10, target: self, selector: "stopScan", userInfo: nil, repeats: false)
    }
    
    func stopScan(){
        print("Stopping")
        self.centralManager?.stopScan()
    }
    
    func centralManager(central: CBCentralManager, didDiscoverPeripheral peripheral: CBPeripheral, advertisementData: [String : AnyObject], RSSI: NSNumber) {
        print("*************************")
        print("Name: \(peripheral.name)")
        print("UUID: \(peripheral.identifier.UUIDString)")
        print("Add Data: \(advertisementData)")
        print("RSSI: \(RSSI)")
        print("*************************")
        if !self.peripherals.contains(peripheral){
            self.peripherals.append(peripheral)
            self.tableView.reloadData()
        }
        
        
    }
    
    func centralManagerDidUpdateState(central: CBCentralManager) {
        if central.state == CBCentralManagerState.PoweredOn{
            print("Everything is Okay")
            startScan()
        }else{
            let alertVC = UIAlertController(title: "Bluetooth Not Working", message: "Check if its turned on", preferredStyle: UIAlertControllerStyle.Alert)
            print("Something is Wrong")
            self.presentViewController(alertVC, animated: true, completion: nil)
            
        }
    }


}


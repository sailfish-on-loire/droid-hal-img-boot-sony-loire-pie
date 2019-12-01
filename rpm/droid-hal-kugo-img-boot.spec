%define device kugo

%define mkbootimg_cmd mkbootimg --ramdisk %{initrd}  --kernel %{kernel} --base 0x80000000 --pagesize 2048 --os_version 9 --os_patch_level 2019-08-01 --cmdline "lpm_levels.sleep_disabled=1 user_debug=31 androidboot.bootdevice=7824900.sdhci androidboot.selinux=permissive msm_rtb.filter=0x3F ehci-hcd.park=3 dwc3.maximum_speed=high dwc3_msm.prop_chg_detect=Y coherent_pool=8M sched_enable_power_aware=1 androidboot.hardware=kugo zram.num_devices=4"  --output

%define root_part_label userdata
%define factory_part_label system

%define display_brightness_path /sys/class/leds/lcd-backlight/brightness
%define display_brightness 16

%include initrd/droid-hal-device-img-boot.inc

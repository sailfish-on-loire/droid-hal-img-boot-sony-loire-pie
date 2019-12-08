%define device suzu

%define mkbootimg_cmd mkbootimg --cmdline "lpm_levels.sleep_disabled=1 user_debug=31 androidboot.bootdevice=7824900.sdhci androidboot.selinux=permissive msm_rtb.filter=0x3F ehci-hcd.park=3 dwc3.maximum_speed=high dwc3_msm.prop_chg_detect=Y coherent_pool=8M sched_enable_power_aware=1 cgroup.memory=nokmem printk.devkmsg=on kpti=0 androidboot.hardware=suzu" --ramdisk %{initrd}  --kernel %{kernel} --base 0x20000000 --pagesize 4096 --kernel_offset 0x00008000 --os_version 9 --os_patch_level 2019-08-01 --ramdisk_offset 0x02000000 --second_offset 0x00f00000 --tags_offset 0x01e00000 --board '' --output

%define root_part_label userdata
%define factory_part_label system

%define display_brightness_path /sys/class/leds/lcd-backlight/brightness
%define display_brightness 16

%include initrd/droid-hal-device-img-boot.inc

#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

Name:       bluetooth-rpi3
Version:    0.1
Release:    1%{?dist}
Summary:    Service and udev rule for Raspberry Pi 3 bluetooth
Group:      System Environment/Kernel
License:	GPLv2+
URL:        https://github.com/fedberry/bluetooth-rpi3
Source0:    brcm43438.service
Source1:    50-bluetooth-hci-auto-poweron.rules

BuildArch:  noarch
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:   bluez >= 5.39-2
Requires:   bcm43438-firmware


%description
Service and udev rule for Raspberry Pi 3 bluetooth support

%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} .

%build


%install
#systemd service
%{__install} -d %{buildroot}/%{_unitdir}
%{__install} -p -m0644 brcm43438.service %{buildroot}/%{_unitdir}

#udev rule
%{__install} -d %{buildroot}/%{_udevrulesdir}
%{__install} -p -m0644 50-bluetooth-hci-auto-poweron.rules %{buildroot}/%{_udevrulesdir}


%clean
rm -rf %{buildroot}


%post
%systemd_post brcm43438.service


%preun
%systemd_preun brcm43438.service


%postun
%systemd_postun brcm43438.service


%files
%attr(0644,root,root) %{_unitdir}/*.service
%attr(0644,root,root) %{_udevrulesdir}/*.rules


%changelog
* Wed May 18 2016 Vaughan <devel at agrez dot net> - 0.1-1
- Initial package

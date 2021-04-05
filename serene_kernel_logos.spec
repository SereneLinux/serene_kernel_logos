Name:           serene_kernel_logos
Version:        0.0.0.1
Release:        1%{?dist}
Summary:        flast exo

Group:          System Environment/Base
License:        GPLv2

URL:            https://fascode.net

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:       serenelinux-icon

%description
This package contains refind cp script

%prep

%build

%install
rm -rf rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/usr/lib/kernel/install.d/
cat <<EOF > %{buildroot}/usr/lib/kernel/install.d/99-serenecopy.install

COMMAND="$1"
KERNEL_VERSION="$2"
ENTRY_DIR_ABS="$3"
KERNEL_IMAGE="$4"
INITRD_OPTIONS_START="5"

if ! [[ $KERNEL_INSTALL_MACHINE_ID ]]; then
    exit 0
fi

if ! [[ -d "$ENTRY_DIR_ABS" ]]; then
    exit 0
fi

MACHINE_ID=$KERNEL_INSTALL_MACHINE_ID

BOOT_ROOT=${ENTRY_DIR_ABS%/$MACHINE_ID/$KERNEL_VERSION}
BOOT_MNT=$(stat -c %m $BOOT_ROOT)
ENTRY_DIR=/${ENTRY_DIR_ABS#$BOOT_MNT}

if [[ $COMMAND == remove ]]; then
    rm -f "$BOOT_ROOT/vmlinuz-${KERNEL_VERSION}.png"
    exit 0
fi

if ! [[ $COMMAND == add ]]; then
    exit 1
fi

if ! [[ $KERNEL_IMAGE ]]; then
    exit 1
fi
cp -f /usr/share/pixmaps/serene/icon_circle.png  "$BOOT_ROOT/vmlinuz-${KERNEL_VERSION}.png"


EOF

%clean
rm -rf rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/kernel/install.d/99-serenecopy.install

%changelog
* 2020/04/05 Mon kokkiemouse <kokkiemouse@fascode.net> - 0.0.0.1
- Create Package
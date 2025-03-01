#  tgcalls - Python binding for tgcalls (c++ lib by Telegram)
#  pytgcalls - Library connecting python binding for tgcalls and Pyrogram
#  Copyright (C) 2020-2021 Il`ya (Marshal) <https://github.com/MarshalX>
#
#  This file is part of tgcalls and pytgcalls.
#
#  tgcalls and pytgcalls is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  tgcalls and pytgcalls is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License v3
#  along with tgcalls. If not, see <http://www.gnu.org/licenses/>.

from typing import Union, Optional

import pyrogram

from pytgcalls import GroupCallNative


class GroupCallDevice(GroupCallNative):
    def __init__(
        self,
        client: Union[pyrogram.Client, None] = None,
        audio_input_device: Optional[str] = None,
        audio_output_device: Optional[str] = None,
        enable_logs_to_console=False,
        path_to_log_file=None,
    ):
        super().__init__(client, enable_logs_to_console, path_to_log_file)

        self.__is_playout_paused = False
        self.__is_recording_paused = False

        self.__raw_audio_device_descriptor = None

        self.__audio_input_device = audio_input_device or ''
        self.__audio_output_device = audio_output_device or ''

    def _setup_and_start_group_call(self):
        self._start_native_group_call(self.__audio_input_device, self.__audio_output_device)

    @property
    def audio_input_device(self):
        """Get audio input device name or GUID

        Note:
            To get system recording device list you can use `print_available_recording_devices()` method.
        """

        return self.__audio_input_device

    @audio_input_device.setter
    def audio_input_device(self, name=None):
        self.set_audio_input_device(name)

    @property
    def audio_output_device(self):
        """Get audio output device name or GUID

        Note:
            To get system playout device list you can use `print_available_playout_devices()` method.
        """

        return self.__audio_output_device

    @audio_output_device.setter
    def audio_output_device(self, name=None):
        self.set_audio_output_device(name)

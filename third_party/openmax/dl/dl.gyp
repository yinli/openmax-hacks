#  Copyright (c) 2013 The WebRTC project authors. All Rights Reserved.
#
#  Use of this source code is governed by a BSD-style license
#  that can be found in the LICENSE file in the root of the source
#  tree. An additional intellectual property rights grant can be found
#  in the file PATENTS.  All contributing project authors may
#  be found in the AUTHORS file in the root of the source tree.

{
  'variables' : {
    # Override this value to build with small float FFT tables
    'big_float_fft%' : 1,
  },
  'targets': [
    {
      'target_name': 'openmax_dl',
      'type': 'static_library',
      'include_dirs': [
        '../',
      ],
      'cflags!': [
        '-mfpu=vfpv3-d16',
      ],
      'cflags': [
        # We enable Neon instructions even with arm_neon==0, to support
        # runtime detection.
        '-mfpu=neon',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../',
        ],
      },
      'sources': [
        'api/arm/armCOMM_s.h',
        'api/arm/armOMX.h',
        'api/arm/omxtypes_s.h',
        'api/omxtypes.h',
        'sp/api/armSP.h',
        'sp/api/omxSP.h',
        # Common C code that can be shared between different
        # architectures.
        'sp/src/armSP_FFT_F32TwiddleTable.c',

        # Common C code for NEON and non-NEON implementations.
        'sp/src/arm/armSP_FFT_S32TwiddleTable.c',
        'sp/src/arm/omxSP_FFTGetBufSize_C_SC32.c',
        'sp/src/arm/omxSP_FFTInit_C_SC32.c',
        'sp/src/arm/omxSP_FFTGetBufSize_R_S32.c',
        'sp/src/arm/omxSP_FFTInit_R_S32.c',
        'sp/src/arm/omxSP_FFTInit_C_SC16.c',
        'sp/src/arm/omxSP_FFTGetBufSize_C_SC16.c',
        'sp/src/arm/omxSP_FFTGetBufSize_R_S16.c',
        'sp/src/arm/omxSP_FFTInit_R_S16.c',
        'sp/src/arm/omxSP_FFTGetBufSize_R_S16S32.c',
        'sp/src/arm/omxSP_FFTInit_R_S16S32.c',
        'sp/src/arm/omxSP_FFTGetBufSize_C_FC32.c',
        'sp/src/arm/omxSP_FFTInit_C_FC32.c',
        'sp/src/arm/omxSP_FFTGetBufSize_R_F32.c',
        'sp/src/arm/omxSP_FFTInit_R_F32.c',

        # NEON-specific implementation
        # Complex 32-bit fixed-point FFT.
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix2_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix2_ls_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix2_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix4_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix4_ls_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix2_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix4_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC32_Radix8_fs_unsafe_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CToC_SC32_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTFwd_CToC_SC32_Sfs_s.S',
        # Real 32-bit fixed-point FFT
        'sp/src/arm/neon/armSP_FFTInv_CCSToR_S32_preTwiddleRadix2_unsafe_s.S',
        'sp/src/arm/neon/omxSP_FFTFwd_RToCCS_S32_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CCSToR_S32_Sfs_s.S',
        # Complex 16-bit fixed-point FFT
        'sp/src/arm/neon/armSP_FFTInv_CCSToR_S16_preTwiddleRadix2_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix2_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix2_ls_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix2_ps_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix2_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix4_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix4_ls_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix4_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_SC16_Radix8_fs_unsafe_s.S',
        'sp/src/arm/neon/omxSP_FFTFwd_CToC_SC16_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CToC_SC16_Sfs_s.S',
        # Real 16-bit fixed-point FFT
        'sp/src/arm/neon/omxSP_FFTFwd_RToCCS_S16_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CCSToR_S16_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTFwd_RToCCS_S16S32_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CCSToR_S32S16_Sfs_s.S',
        # Complex floating-point FFT
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix2_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix2_ls_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix2_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix4_fs_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix4_ls_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix2_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix4_unsafe_s.S',
        'sp/src/arm/neon/armSP_FFT_CToC_FC32_Radix8_fs_unsafe_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CToC_FC32_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTFwd_CToC_FC32_Sfs_s.S',
        # Real floating-point FFT
        'sp/src/arm/neon/armSP_FFTInv_CCSToR_F32_preTwiddleRadix2_unsafe_s.S',
        'sp/src/arm/neon/omxSP_FFTFwd_RToCCS_F32_Sfs_s.S',
        'sp/src/arm/neon/omxSP_FFTInv_CCSToR_F32_Sfs_s.S',
      ],
      'conditions' : [
        ['big_float_fft == 1', {
          'defines': [
            'BIG_FFT_TABLE',
          ],
        }],
      ],
  }]
}

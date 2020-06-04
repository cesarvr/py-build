const { spawn } = require('child_process');

function pull(action, remote, branch) {
  console.log(`pulling: ${Date.now()},  from ${remote}:${branch}`)
  const git = spawn('git', ['pull', remote, branch])

  git.stdout.on('data', function(data) {
    let msg = data.toString()
    console.log('[git pull]: ', msg)

    if(!msg.includes('Already up to date.')){ 
      action()
    }
  })

  git.on('exit', function(data) {
    console.log('[git pull]: exit ', data)
  })
}

function push(remote, branch) {
  const git = spawn('git', ['push', remote, branch])
  console.log(`pushing: ${Date.now()}, from ${remote}:${branch}`)

  git.stdout.on('data', function(data) {
    let msg = data.toString()
    console.log('[git error]: ', data)
  })

  git.on('data', function(data) {
    console.log('[git push]: ', data)
  })

  git.on('exit', function(data) {
    console.log('[git push]: exit ', data)
  })
}


setInterval( () =>
  pull(() => push('gogs','master'), 'origin', 'master'),
20000)
